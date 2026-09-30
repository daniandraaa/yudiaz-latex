import pytest
from pathlib import Path
from fastapi.testclient import TestClient
from backend.main import app, storage

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["app"] == "Yudiaz LaTeX Studio"

def test_templates_endpoint():
    response = client.get("/api/templates")
    assert response.status_code == 200
    templates = response.json()
    assert len(templates) >= 4
    template_ids = [t["id"] for t in templates]
    assert "blank" in template_ids
    assert "proposal" in template_ids
    assert "paper" in template_ids

def test_folder_crud():
    # 1. Create folder
    create_resp = client.post("/api/folders", json={"name": "Test Folder", "color": "#10b981"})
    assert create_resp.status_code == 200
    folder_data = create_resp.json()
    folder_id = folder_data["id"]
    assert folder_data["name"] == "Test Folder"

    # 2. List folders
    list_resp = client.get("/api/folders")
    assert list_resp.status_code == 200
    folders = list_resp.json()
    assert any(f["id"] == folder_id for f in folders)

    # 3. Update folder
    update_resp = client.put(f"/api/folders/{folder_id}", json={"name": "Updated Test Folder"})
    assert update_resp.status_code == 200
    assert update_resp.json()["name"] == "Updated Test Folder"

    # 4. Delete folder
    del_resp = client.delete(f"/api/folders/{folder_id}")
    assert del_resp.status_code == 200
    assert del_resp.json()["success"] is True

def test_project_create_and_compile():
    # Create project with blank template
    resp = client.post("/api/projects", json={
        "title": "Automated Test Project",
        "description": "Integration test for compiler",
        "template": "blank"
    })
    assert resp.status_code == 200
    proj = resp.json()
    proj_id = proj["id"]
    assert proj["title"] == "Automated Test Project"

    # Verify files
    detail_resp = client.get(f"/api/projects/{proj_id}")
    assert detail_resp.status_code == 200
    files_data = detail_resp.json()
    assert any(f["name"] == "main.tex" for f in files_data["files"])

    # Compile project
    comp_resp = client.post(f"/api/projects/{proj_id}/compile")
    assert comp_resp.status_code == 200
    comp_res = comp_resp.json()
    assert comp_res["success"] is True
    assert comp_res["status"] == "success"

    # Check PDF download
    pdf_resp = client.get(f"/api/projects/{proj_id}/pdf")
    assert pdf_resp.status_code == 200
    assert pdf_resp.headers["content-type"] == "application/pdf"
    assert len(pdf_resp.content) > 1000  # valid PDF file

    # Check online public preview
    share_id = proj["share_id"]
    preview_page_resp = client.get(f"/preview/{share_id}")
    assert preview_page_resp.status_code == 200
    assert "Automated Test Project" in preview_page_resp.text

    shared_pdf_resp = client.get(f"/api/preview/{share_id}/pdf")
    assert shared_pdf_resp.status_code == 200
    assert shared_pdf_resp.headers["content-type"] == "application/pdf"

    # Clean up test project
    del_p_resp = client.delete(f"/api/projects/{proj_id}")
    assert del_p_resp.status_code == 200

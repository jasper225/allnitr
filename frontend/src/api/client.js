const API_BASE = "http://localhost:8000/api/v1";

export async function uploadFile(file) {
    const form = new FormData();
    form.append('file', file);

    const response = await fetch(`${API_BASE}/pipeline/`, {
        method: 'POST',
        body: form,
    });

    if (!response.ok) throw new Error('File upload failed');
    return response.json();
}
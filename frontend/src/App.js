document.getElementById('upload-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const fileInput = document.getElementById('file-input');
    const file = fileInput.files[0];

    const formData = new FormData();
    formData.append('file', file);

    const response = await fetch('http://localhost:5000/upload', {
        method: 'POST',
        body: formData,
    });

    if (response.ok) {
        const blob = await response.blob();
        const translatedUrl = URL.createObjectURL(blob);

        document.getElementById('translated-image').src = translatedUrl;
        document.getElementById('original-image').src = URL.createObjectURL(file);
    } else {
        console.error('Failed to upload or process the image');
    }
});
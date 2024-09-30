async function uploadImage() {
  const fileInput = document.getElementById('fileUpload');
  const file = fileInput.files[0];
  if (!file) {
    alert('Please select a file.');
    return;
  }

  const reader = new FileReader();
  reader.onloadend = async function () {
    const base64Data = reader.result.split(',')[1]; // Extract base64 part
    try {
      const response = await fetch(
        'https://your-api-gateway-endpoint/dev/upload',
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            // 'x-api-key': 'YOUR_API_KEY', // Uncomment if API Key is required
            // 'Authorization': 'Bearer YOUR_JWT_TOKEN' // Uncomment if using auth
          },
          body: JSON.stringify({
            image_data: base64Data,
            image_name: file.name,
          }),
        }
      );

      if (response.ok) {
        const result = await response.json();
        console.log('Upload successful:', result);
        alert('Image uploaded successfully!');
      } else {
        const error = await response.json();
        console.error('Upload failed:', error);
        alert(`Upload failed: ${error.message || 'Unknown error'}`);
      }
    } catch (error) {
      console.error('Error uploading image:', error);
      alert('An error occurred while uploading the image.');
    }
  };
  reader.readAsDataURL(file);
}

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

const API_URL = 'http://localhost:8000/api';

function App() {
  const [photos, setPhotos] = useState([]);
  const [selectedFile, setSelectedFile] = useState(null);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [uploading, setUploading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchPhotos();
  }, []);

  const fetchPhotos = async () => {
    try {
      const response = await axios.get(`${API_URL}/photos/`);
      setPhotos(response.data.photos);
    } catch (error) {
      console.error('Error fetching photos:', error);
      setError('Failed to fetch photos. Make sure the backend is running.');
    }
  };

  const handleFileSelect = (event) => {
    setSelectedFile(event.target.files[0]);
    setError('');
  };

  const handleUpload = async (e) => {
    e.preventDefault();
    
    if (!selectedFile) {
      setError('Please select a file');
      return;
    }

    setUploading(true);
    setError('');
    const response = await fetch(`http://localhost:8000/api/get-upload-url/?file_name=${selectedFile.name}`);
    const data = await response.json();
      
      if (!data.url) {
        throw new Error('Failed to get upload URL');
      }

    console.log("Got Presigned URL:", data.url);
    const formData = new FormData();
    formData.append('file', selectedFile);
    formData.append('title', title || selectedFile.name);
    formData.append('description', description);

    try {
      // await axios.post(`${API_URL}/photos/`, formData, {
      //   headers: {
      //     'Content-Type': 'multipart/form-data',
      //   },
      // });
      const result = await fetch(data.url, {
        method: 'PUT',
        body: selectedFile,
        headers: {
          'Content-Type': selectedFile.type // Important: Must match what you signed in Django
        }
      });
      
      // Reset form
      setSelectedFile(null);
      setTitle('');
      setDescription('');
      document.getElementById('file-input').value = '';
      
      // Refresh photos
      fetchPhotos();
    } catch (error) {
      console.error('Error uploading photo:', error);
      setError('Failed to upload photo. Make sure LocalStack is running.');
    } finally {
      setUploading(false);
    }
  };

  const handleDelete = async (id) => {
    if (!window.confirm('Are you sure you want to delete this photo?')) {
      return;
    }

    try {
      await axios.delete(`${API_URL}/photos/${id}/`);
      fetchPhotos();
    } catch (error) {
      console.error('Error deleting photo:', error);
      setError('Failed to delete photo');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>🏯 The Great Wall of Photos</h1>
        <p className="subtitle">React + Django + LocalStack Photo Gallery</p>
      </header>

      <div className="container">
        <div className="upload-section">
          <h2>Upload New Photo</h2>
          <form onSubmit={handleUpload}>
            <div className="form-group">
              <label htmlFor="file-input">Choose Image:</label>
              <input
                id="file-input"
                type="file"
                accept="image/*"
                onChange={handleFileSelect}
                disabled={uploading}
              />
            </div>

            <div className="form-group">
              <label htmlFor="title-input">Title (optional):</label>
              <input
                id="title-input"
                type="text"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                placeholder="Enter photo title"
                disabled={uploading}
              />
            </div>

            <div className="form-group">
              <label htmlFor="description-input">Description (optional):</label>
              <textarea
                id="description-input"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                placeholder="Enter photo description"
                disabled={uploading}
                rows="3"
              />
            </div>

            {error && <div className="error-message">{error}</div>}

            <button type="submit" disabled={uploading || !selectedFile}>
              {uploading ? 'Uploading...' : 'Upload Photo'}
            </button>
          </form>
        </div>

        <div className="gallery-section">
          <h2>Photo Gallery ({photos.length})</h2>
          {photos.length === 0 ? (
            <p className="no-photos">No photos yet. Upload your first photo!</p>
          ) : (
            <div className="photo-grid">
              {photos.map((photo) => (
                <div key={photo.id} className="photo-card">
                  <img src={photo.image_url} alt={photo.title} />
                  <div className="photo-info">
                    <h3>{photo.title}</h3>
                    {photo.description && <p>{photo.description}</p>}
                    <div className="photo-meta">
                      <small>{new Date(photo.uploaded_at).toLocaleString()}</small>
                    </div>
                    <button 
                      className="delete-btn"
                      onClick={() => handleDelete(photo.id)}
                    >
                      Delete
                    </button>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;

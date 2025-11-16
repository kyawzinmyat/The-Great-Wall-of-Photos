# Application Screenshots & Features

## Home Page / Photo Gallery

The application is a **single-page application** with two main sections:

### 1. Upload Section (Top)
- **File Input**: Choose an image file from your computer
- **Title Field**: Optional text input for photo title (auto-filled with filename if left empty)
- **Description Field**: Optional textarea for photo description
- **Upload Button**: Submit button that shows "Uploading..." while processing
- **Error Messages**: Displays in red if upload fails

**Visual Design:**
- White card with rounded corners
- Purple gradient header "Upload New Photo"
- Clean form with labeled inputs
- Purple gradient upload button
- Error messages with red border

### 2. Gallery Section (Bottom)
- **Photo Count**: Shows total number of photos in header
- **Grid Layout**: Responsive grid (3 columns on desktop, 1 on mobile)
- **Photo Cards**: Each photo displayed in a card with:
  - Image (250px height, maintains aspect ratio)
  - Title in bold
  - Description text
  - Upload timestamp
  - Red "Delete" button

**Visual Design:**
- White card with rounded corners
- Purple gradient header "Photo Gallery (X)"
- Grid layout with 25px gap between cards
- Cards have hover effect (lift up on hover)
- Empty state message when no photos

### Overall Theme
- **Background**: Purple gradient (from #667eea to #764ba2)
- **Primary Color**: Purple gradient
- **Text**: Dark gray on white backgrounds
- **Cards**: White with subtle shadows
- **Buttons**: Purple gradient or red for delete
- **Responsive**: Works on mobile, tablet, and desktop

## User Flow

1. **User opens app** → Sees upload form and empty gallery (or existing photos)
2. **User clicks "Choose Image"** → File picker opens
3. **User selects photo** → File name appears in input
4. **User optionally adds title/description** → Text fields update
5. **User clicks "Upload Photo"** → 
   - Button shows "Uploading..."
   - Photo uploads to S3 via Django API
   - Gallery refreshes with new photo
   - Form resets
6. **User views photos in gallery** → Grid of uploaded photos
7. **User clicks "Delete"** → 
   - Confirmation dialog appears
   - If confirmed, photo removed from S3 and database
   - Gallery refreshes

## Technical Features

- **Real-time Updates**: Gallery refreshes after upload/delete
- **Error Handling**: User-friendly error messages
- **Loading States**: Buttons show loading text during operations
- **Form Validation**: Prevents upload without file selected
- **Responsive Images**: Photos maintain aspect ratio
- **Timestamps**: Shows when each photo was uploaded
- **Clean URLs**: S3 URLs point to LocalStack (http://localhost:4566)

## Color Palette

```
Primary Gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%)
Background: Same gradient
Cards: #ffffff (white)
Text: #333333 (dark gray)
Secondary Text: #666666, #999999
Delete Button: #e74c3c (red)
Borders: #e0e0e0 (light gray)
Focus/Hover: #667eea (purple)
```

## Typography

- **Headers**: Bold, 2-3rem for main title, 1.3rem for photo titles
- **Body Text**: 1rem, sans-serif system fonts
- **Buttons**: 1.1rem, bold
- **Meta Text**: 0.85-0.9rem

## Accessibility Features

- Labeled form inputs with `htmlFor`
- Button disabled states
- Focus indicators on form fields
- High contrast text on backgrounds
- Descriptive button text
- Alt text on images

## Performance

- Photos lazy-loaded from S3
- Minimal dependencies (React, Axios, Django, boto3)
- Optimized build with Create React App
- No unnecessary re-renders
- Efficient state management

## Browser Support

Works on all modern browsers:
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

---

**Note**: To see the actual application, run both the Django backend and React frontend, then navigate to http://localhost:3000

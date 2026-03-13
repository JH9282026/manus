# X Ads Creative Specifications

## Image Specifications

### Standard Image Ads
- **Format**: JPG, PNG
- **File Size**: Max 5MB
- **Dimensions**: 1200x628px (recommended)
- **Aspect Ratio**: 1.91:1 (landscape), 1:1 (square)
- **Safe Zone**: Keep text/logos in center 80%
- **Color Space**: sRGB
- **Resolution**: 72 DPI minimum

### Image Best Practices
- Use high-contrast colors
- Minimal text (< 20% of image)
- Clear focal point
- Mobile-optimized (test at small sizes)
- Brand logo in corner

## Video Specifications

### Standard Video Ads
- **Format**: MP4, MOV
- **File Size**: Max 1GB
- **Length**: 2:20 maximum (15s recommended for awareness, 30s for consideration)
- **Resolution**: 1920x1080 (16:9) or 1080x1080 (1:1)
- **Frame Rate**: 30 or 60 fps
- **Bitrate**: 6,000-10,000 kbps
- **Audio**: AAC, 128 kbps minimum

### Video Best Practices
- Hook in first 3 seconds
- Captions for sound-off viewing
- Vertical or square for mobile
- Clear CTA at end
- Brand early (within 3s)

## Twitter Card Types

### Website Card
- **Image**: 800x418px minimum (1.91:1)
- **Title**: 70 characters max
- **Description**: 200 characters max
- **URL**: Any valid URL
- **CTA**: Predefined options (Learn More, Shop Now, etc.)

### App Download Card
- **Image**: 800x800px (1:1)
- **App Name**: Auto-populated from store
- **Description**: 256 characters max
- **Deep Link**: Optional
- **Supported Platforms**: iOS, Android

### Video Website Card
- **Video**: Same specs as standard video
- **Title**: 70 characters max
- **URL**: Landing page
- **CTA**: Predefined options

### Conversation Card
- **Image**: 800x418px (1.91:1)
- **Title**: 23 characters max
- **First CTA**: 20 characters max
- **Second CTA**: 20 characters max
- **Third CTA**: 20 characters max (optional)
- **Fourth CTA**: 20 characters max (optional)
- **Thank You Text**: 23 characters max
- **Thank You URL**: Optional landing page

## Text Specifications

### Tweet Text
- **Length**: 280 characters max
- **Links**: Count as 23 characters (auto-shortened)
- **Media**: Doesn't count toward character limit
- **Hashtags**: 1-2 recommended, count toward limit
- **Mentions**: Count toward limit

### Card Text
- **Website Title**: 70 characters max
- **Description**: 200 characters max
- **CTA Button**: Predefined text options

## Media Upload Process

### Image Upload
```python
import base64
import requests

def upload_image(image_path, access_token):
    with open(image_path, "rb") as f:
        image_data = base64.b64encode(f.read()).decode()
    
    response = requests.post(
        "https://upload.twitter.com/1.1/media/upload.json",
        headers={"Authorization": f"Bearer {access_token}"},
        data={
            "media_data": image_data,
            "media_category": "tweet_image"
        }
    )
    
    return response.json()["media_id_string"]
```

### Video Upload (Chunked)
```python
import os

def upload_video(video_path, access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    
    # INIT
    file_size = os.path.getsize(video_path)
    init_response = requests.post(
        "https://upload.twitter.com/1.1/media/upload.json",
        headers=headers,
        data={
            "command": "INIT",
            "media_type": "video/mp4",
            "total_bytes": file_size,
            "media_category": "amplify_video"
        }
    )
    media_id = init_response.json()["media_id_string"]
    
    # APPEND
    with open(video_path, "rb") as f:
        segment_id = 0
        while True:
            chunk = f.read(5 * 1024 * 1024)  # 5MB chunks
            if not chunk:
                break
            
            requests.post(
                "https://upload.twitter.com/1.1/media/upload.json",
                headers=headers,
                files={"media": chunk},
                data={
                    "command": "APPEND",
                    "media_id": media_id,
                    "segment_index": segment_id
                }
            )
            segment_id += 1
    
    # FINALIZE
    requests.post(
        "https://upload.twitter.com/1.1/media/upload.json",
        headers=headers,
        data={
            "command": "FINALIZE",
            "media_id": media_id
        }
    )
    
    return media_id
```

## Creative Optimization Tips

### Image Optimization
1. **Compress without quality loss** - Use tools like TinyPNG
2. **Test multiple variations** - Different colors, layouts, CTAs
3. **Mobile-first design** - 80% of X users on mobile
4. **Contrast for readability** - High contrast text on images
5. **Consistent branding** - Logo, colors, fonts

### Video Optimization
1. **Hook immediately** - First 3 seconds critical
2. **Sound-off friendly** - 85% watch without sound
3. **Vertical or square** - Better mobile experience
4. **Short and focused** - 15s for awareness, 30s max for consideration
5. **Clear CTA** - Tell viewers what to do next

### Text Optimization
1. **Front-load value** - Key message in first 100 characters
2. **Use emojis sparingly** - 1-2 max, relevant to message
3. **Clear CTA** - One specific action
4. **Avoid jargon** - Simple, conversational language
5. **Test variations** - A/B test different copy angles

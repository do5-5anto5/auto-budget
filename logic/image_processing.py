"""
Image processing logic for logo compression and conversion.
"""

import base64
import io
import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
from PIL import Image


def resize_image_for_logo(image_path: str, max_size: tuple = (160, 160)) -> str:
    """
    Resize image to fit logo dimensions and convert to base64.
    
    Args:
        image_path: Path to the image file
        max_size: Maximum dimensions (width, height) for the logo
        
    Returns:
        Base64 encoded image string
    """
    try:
        # Open and resize image
        with Image.open(image_path) as img:
            # Convert to RGB if necessary (for PNG with transparency)
            if img.mode in ('RGBA', 'LA', 'P'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background
            
            # Detect image shape and adapt processing
            original_ratio = img.width / img.height
            is_wide = original_ratio > 1.0  # Wider than tall
            is_tall = original_ratio < 1.0  # Taller than wide
            
            if is_wide:
                # Wide image - use landscape orientation
                target_size = (120, 90)  # 4:3 ratio
            elif is_tall:
                # Tall image - use portrait orientation  
                target_size = (90, 120)  # 3:4 ratio
            else:
                # Square image - keep square
                target_size = max_size
            
            # Process image to fit its natural shape
            img_ratio = img.width / img.height
            target_ratio = target_size[0] / target_size[1]
            
            if img_ratio > target_ratio:
                # Image is wider than target - crop height
                new_height = int(img.width / target_ratio)
                top = (img.height - new_height) // 2
                img = img.crop((0, top, img.width, top + new_height))
            else:
                # Image is taller than or equal to target - crop width
                new_width = int(img.height * target_ratio)
                left = (img.width - new_width) // 2
                img = img.crop((left, 0, left + new_width, img.height))

            # Resize to target dimensions
            img = img.resize(target_size, Image.Resampling.LANCZOS)
            
            # Store shape info for UI adaptation
            shape_info = {
                'is_wide': is_wide,
                'is_tall': is_tall,
                'actual_size': target_size
            }
            
            # Convert to bytes
            img_buffer = io.BytesIO()
            img.save(img_buffer, format='JPEG', quality=90, optimize=True)
            img_bytes = img_buffer.getvalue()
            
            # Convert to base64
            base64_str = base64.b64encode(img_bytes).decode('utf-8')
            return base64_str
            
    except Exception as e:
        print(f"Error processing image: {e}")
        return ""


def base64_to_pil_image(base64_str: str) -> Image.Image:
    """
    Convert base64 string to PIL Image.
    
    Args:
        base64_str: Base64 encoded image string
        
    Returns:
        PIL Image instance or None if failed
    """
    try:
        if not base64_str:
            return None
            
        # Decode base64
        img_bytes = base64.b64decode(base64_str)
        
        # Create PIL Image
        img = Image.open(io.BytesIO(img_bytes))
        return img
        
    except Exception as e:
        print(f"Error converting base64 to PIL Image: {e}")
        return None


def base64_to_ctk_image(base64_str: str, size: tuple = (100, 100)) -> ctk.CTkImage:
    """
    Convert base64 string to CTkImage for display in UI.
    
    Args:
        base64_str: Base64 encoded image string
        size: Size for the CTkImage
        
    Returns:
        CTkImage instance or None if failed
    """
    try:
        if not base64_str:
            return None
            
        # Convert to PIL Image first
        pil_img = base64_to_pil_image(base64_str)
        
        if pil_img:
            # Create CTkImage
            ctk_img = ctk.CTkImage(pil_img, size=size)
            return ctk_img
        
        return None
        
    except Exception as e:
        print(f"Error converting base64 to CTkImage: {e}")
        return None


def select_image_file(parent_widget=None) -> str:
    """
    Open file dialog to select an image file.
    
    Args:
        parent_widget: Parent widget for the dialog
        
    Returns:
        Selected file path or empty string if cancelled
    """
    file_types = [
        ("Image files", "*.jpg *.jpeg *.png *.gif *.bmp *.tiff"),
        ("JPEG files", "*.jpg *.jpeg"),
        ("PNG files", "*.png"),
        ("All files", "*.*")
    ]
    
    file_path = filedialog.askopenfilename(
        title="Selecione o logo da empresa",
        filetypes=file_types,
        parent=parent_widget
    )
    
    return file_path


def base64_to_pil_image(base64_str: str) -> Image.Image:
    """
    Convert base64 image to PIL Image.
    
    Args:
        base64_str: Base64 encoded image string
        
    Returns:
        PIL Image instance or None if failed
    """
    try:
        if not base64_str:
            return None
            
        # Decode base64
        img_bytes = base64.b64decode(base64_str)
        img_buffer = io.BytesIO(img_bytes)
        
        # Create PIL Image
        pil_img = Image.open(img_buffer)
        return pil_img
        
    except Exception as e:
        print(f"Error converting base64 to PIL Image: {e}")
        return None


def validate_image_file(file_path: str) -> bool:
    """
    Validate if the file is a supported image format.
    
    Args:
        file_path: Path to the image file
        
    Returns:
        True if valid image format, False otherwise
    """
    try:
        with Image.open(file_path) as img:
            img.verify()
        return True
    except Exception:
        return False

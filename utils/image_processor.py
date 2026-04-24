"""
Image processing utilities for logo upload and resizing.
"""

import base64
import io
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk


def resize_image_for_logo(image_path: str, max_size: tuple = (120, 120)) -> str:
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
            
            # Resize maintaining aspect ratio
            img.thumbnail(max_size, Image.Resampling.LANCZOS)
            
            # Convert to bytes
            img_buffer = io.BytesIO()
            img.save(img_buffer, format='JPEG', quality=85)
            img_bytes = img_buffer.getvalue()
            
            # Convert to base64
            base64_str = base64.b64encode(img_bytes).decode('utf-8')
            return base64_str
            
    except Exception as e:
        print(f"Error processing image: {e}")
        return ""


def base64_to_ctk_image(base64_str: str, size: tuple = (80, 80)) -> ctk.CTkImage:
    """
    Convert base64 image to CTkImage for display in UI.
    
    Args:
        base64_str: Base64 encoded image string
        size: Size for the CTkImage
        
    Returns:
        CTkImage instance or None if failed
    """
    try:
        if not base64_str:
            return None
            
        # Decode base64
        img_bytes = base64.b64decode(base64_str)
        img_buffer = io.BytesIO(img_bytes)
        
        # Create PIL Image
        pil_img = Image.open(img_buffer)
        
        # Create CTkImage
        ctk_img = ctk.CTkImage(pil_img, size=size)
        return ctk_img
        
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


def create_logo_display_frame(parent, row: int, column: int, logo_data: str = None) -> tuple:
    """
    Create a frame with clickable avatar for logo upload/display.
    
    Args:
        parent: Parent widget
        row: Grid row position
        column: Grid column position
        logo_data: Base64 encoded logo image data
        
    Returns:
        Tuple of (frame, image_label, update_callback_function)
    """
    # Create frame
    frame = ctk.CTkFrame(parent, corner_radius=8)
    frame.grid(row=row, column=column, pady=10, padx=10, sticky="ew")
    
    # Create label for logo display
    logo_label = ctk.CTkLabel(frame, text="Logo", width=80, height=80)
    logo_label.pack(pady=10, padx=10)
    
    # Update display if logo data exists
    if logo_data:
        ctk_img = base64_to_ctk_image(logo_data, (80, 80))
        if ctk_img:
            logo_label.configure(image=ctk_img, text="")
    
    def update_logo():
        """Handle logo upload/update"""
        file_path = select_image_file(parent)
        if file_path:
            base64_str = resize_image_for_logo(file_path)
            if base64_str:
                # Update display
                ctk_img = base64_to_ctk_image(base64_str, (80, 80))
                if ctk_img:
                    logo_label.configure(image=ctk_img, text="")
                
                # Store in parent for later saving
                parent.temp_logo_image = base64_str
                return base64_str
        return None
    
    # Make label clickable
    logo_label.configure(cursor="hand2")
    logo_label.bind("<Button-1>", lambda e: update_logo())
    
    # Add instruction text
    instruction_label = ctk.CTkLabel(frame, text="Clique para adicionar logo", font=ctk.CTkFont(size=11))
    instruction_label.pack(pady=(0, 10))
    
    return frame, logo_label, update_logo

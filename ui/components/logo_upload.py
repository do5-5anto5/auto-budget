"""
UI components for logo upload and display.
"""

import customtkinter as ctk
from logic.image_processing import base64_to_ctk_image, select_image_file


def create_logo_upload_frame(parent, row: int, column: int, logo_data: str = None, on_logo_update=None):
    """
    Create a logo upload frame with clickable avatar that adapts to image shape.
    
    Args:
        parent: Parent widget
        row: Grid row position
        column: Grid column position
        logo_data: Base64 image data
        on_logo_update: Callback function called when logo is updated
        
    Returns:
        Tuple of (frame, image_label)
    """
    # Detect image shape to adapt UI
    ui_width = 80
    ui_height = 80
    
    # Create frame
    frame = ctk.CTkFrame(parent, corner_radius=8)
    frame.grid(row=row, column=column, pady=10, padx=10, sticky="ew")
    
    # Create label for logo display as circular avatar
    if logo_data:
        # If logo exists, create label with image
        ctk_img = base64_to_ctk_image(logo_data, (100, 100))
        if ctk_img:
            logo_label = ctk.CTkLabel(
                frame, 
                text="", 
                image=ctk_img,
                width=100, 
                height=100,
                corner_radius=0,  # No rounded corners - simple square
                fg_color="transparent"  # No background so image fills the space
            )
        else:
            # Fallback if image loading fails
            logo_label = ctk.CTkLabel(
                frame, 
                text="", 
                width=100, 
                height=100,
                corner_radius=0,  # No rounded corners - simple square
                fg_color="#1a1a1a",  # Black square placeholder
                text_color="#666666"
            )
    else:
        # If no logo, show black square placeholder
        logo_label = ctk.CTkLabel(
            frame, 
            text="", 
            width=100, 
            height=100,
            corner_radius=0,  # No rounded corners - simple square
            fg_color="#1a1a1a",  # Black square placeholder
            text_color="#666666"
        )
    
    logo_label.pack(pady=10, padx=10)
    
    def handle_logo_click():
        """Handle logo upload/update"""
        file_path = select_image_file(parent)
        if file_path:
            from logic.image_processing import resize_image_for_logo
            base64_str = resize_image_for_logo(file_path)
            if base64_str:
                # Update display - create new image
                new_ctk_img = base64_to_ctk_image(base64_str, (100, 100))
                if new_ctk_img:
                    # Update existing label with new image
                    logo_label.configure(
                        image=new_ctk_img, 
                        text="",
                        fg_color="transparent"  # No background so image fills the square
                    )
                
                # Store in parent for later saving
                parent.temp_logo_image = base64_str
                
                # Call callback if provided
                if on_logo_update:
                    on_logo_update(base64_str)
                
                return base64_str
        return None
    
    # Make label clickable
    logo_label.configure(cursor="hand2")
    logo_label.bind("<Button-1>", lambda e: handle_logo_click())
    
    # Add instruction text
    instruction_label = ctk.CTkLabel(frame, text="Clique para adicionar logo", font=ctk.CTkFont(size=11))
    instruction_label.pack(pady=(0, 10))
    
    return frame, logo_label

"""
UI components for logo upload and display.
"""

import customtkinter as ctk
from logic.image_processing import base64_to_ctk_image, select_image_file


def create_logo_upload_frame(parent, row: int, column: int, logo_data: str = None, on_logo_update=None):
    """
    Create a logo upload frame with clickable area that has rounded corners.
    
    Args:
        parent: Parent widget
        row: Grid row position
        column: Grid column position
        logo_data: Base64 image data
        on_logo_update: Callback function called when logo is updated
        
    Returns:
        Tuple of (frame, logo_button)
    """
    # UI Constants
    IMAGE_SIZE = (100, 100)
    CORNER_RADIUS = 15
    
    # Create main container frame
    frame = ctk.CTkFrame(
        parent, 
        corner_radius=CORNER_RADIUS,
        fg_color="#1a1a1a",
        border_width=1,
        border_color="#333333"
    )
    frame.grid(row=row, column=column, pady=15, padx=15, sticky="ew")
    
    # Inner container for the image to ensure centering
    inner_container = ctk.CTkFrame(frame, fg_color="transparent")
    inner_container.pack(pady=20, padx=20)
    
    # Handle initial image
    ctk_img = None
    if logo_data:
        ctk_img = base64_to_ctk_image(logo_data, IMAGE_SIZE, corner_radius=CORNER_RADIUS)
    
    def handle_logo_click():
        """Handle logo upload/update"""
        file_path = select_image_file(parent)
        if file_path:
            from logic.image_processing import resize_image_for_logo
            base64_str = resize_image_for_logo(file_path)
            if base64_str:
                # Update display with rounded corners
                new_ctk_img = base64_to_ctk_image(base64_str, IMAGE_SIZE, corner_radius=CORNER_RADIUS)
                if new_ctk_img:
                    logo_button.configure(image=new_ctk_img, text="")
                
                # Store in parent
                parent.temp_logo_image = base64_str
                
                # Call callback
                if on_logo_update:
                    on_logo_update(base64_str)
                
                return base64_str
        return None
    
    # Create the clickable logo button (instead of a label)
    # This provides better hover feedback and handles rounded backgrounds natively
    logo_button = ctk.CTkButton(
        inner_container,
        text="+" if not ctk_img else "",
        image=ctk_img,
        width=IMAGE_SIZE[0],
        height=IMAGE_SIZE[1],
        corner_radius=CORNER_RADIUS,
        fg_color="#2b2b2b",
        hover_color="#3b3b3b",
        text_color="#888888",
        font=ctk.CTkFont(size=24, weight="bold"),
        command=handle_logo_click
    )
    logo_button.pack()
    
    # Add instruction text
    instruction_label = ctk.CTkLabel(
        frame, 
        text="Clique para alterar logo", 
        font=ctk.CTkFont(size=11),
        text_color="#aaaaaa"
    )
    instruction_label.pack(pady=(0, 15))
    
    return frame, logo_button

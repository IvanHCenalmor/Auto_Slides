from pptx import Presentation
import os

def create_ppt_with_date_and_members(date, save_path, filename, members):
    prs = Presentation("Presentation_template.pptx")
    
    # Edit the first slide
    slide = prs.slides[0]
    title = slide.shapes.title
    subtitle = slide.placeholders[1]
    
    title.text = "5 minutes presentations"
    subtitle.text = f"Date: {date.strftime('%Y-%m-%d')}"
    
    # Create individual slides for each member
    for member in members:
        # Slide for "Previous week"
        slide_layout = prs.slide_layouts[2]  # Use the title and content layout
        slide = prs.slides.add_slide(slide_layout)
        
        title = slide.shapes.title
        title.text = f"{member} - Previous week"
        
        # Slide for "This week"
        slide = prs.slides.add_slide(slide_layout)
        
        title = slide.shapes.title
        title.text = f"{member} - This week"
    
    file_path = os.path.join(save_path, filename)

    if os.path.exists(file_path):
        os.remove(file_path)
    
    prs.save(file_path)

if __name__ == "__main__":
    from datetime import datetime, timedelta

    # List of lab members
    lab_members = ["Guillaume",
                "Gautier",
                "Joanna",
                "Hannah",
                "Jaakko",
                "Ana",
                "Sujan",
                "Sarah",
                "Monika",
                "Marcela",
                "Iván",
                "Johanna"]

    # Generate PowerPoint files with weekly dates and individual slides for each member
    start_date = datetime(2025, 1, 27)
    end_date = datetime(2025, 3, 1)
    current_date = start_date

    save_path = "presentations/"
    os.makedirs(save_path, exist_ok=True)

    while current_date <= end_date:
        filename = f"{current_date.strftime('%Y%m%d')}_5min_Presentaiton.pptx"
        create_ppt_with_date_and_members(current_date, save_path, filename, lab_members)
        current_date += timedelta(weeks=1)
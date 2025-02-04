import click
import time
import os
from colorama import Fore, Style, init
from tqdm import tqdm
from coursegen.generator import create_project_structure, load_structure

# Initialize Colorama for Windows support
init(autoreset=True)

@click.group()
def cli():
    """CourseGen: Udemy Course Management CLI"""
    pass

@cli.command()
@click.argument("course_name")
def create(course_name):
    """🎯 Create a new Udemy course folder structure"""

    print(f"\n{Fore.CYAN}🎯 Generating Udemy Course: {Fore.YELLOW}{course_name}\n")

    # Simulate progress with loading bar
    for _ in tqdm(range(5), desc="Creating course structure...", unit="step"):
        time.sleep(0.5)  

    # Create course structure and get the full path
    course_path = create_project_structure(course_name)

    # Convert path to clickable format for Windows (CMD & PowerShell)
    clickable_path = f"file:///{course_path.replace(os.sep, '/')}"

    # Print visually improved output
    print(f"\n{Fore.GREEN}✅ Course structure created successfully!{Style.RESET_ALL}")
    print(f"{Fore.BLUE}📂 Open your course folder:\n")
    print(f"   {Fore.YELLOW}{clickable_path}{Style.RESET_ALL}\n")
    print(f"📎 {Fore.CYAN}Sections & Lectures Created:{Style.RESET_ALL}")

    structure = load_structure()
    for section, lectures in structure["sections"].items():
        print(f"\n{Fore.MAGENTA}📁 {section.replace('-', ' ')}{Style.RESET_ALL}")
        for lecture in lectures:
            print(f"   📄 {lecture.replace('-', ' ')}")

    print(f"\n📎 {Fore.CYAN}Tip: Click the link above to open your course folder.{Style.RESET_ALL}\n")

if __name__ == "__main__":
    cli()

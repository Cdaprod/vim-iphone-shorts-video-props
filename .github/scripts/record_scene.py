import sys
import time
import os
from asciinema_automation import record_scene
import subprocess
from pyvirtualdisplay import Display

# Set terminal dimensions for vertical video (9:19.5 aspect ratio)
TERM_COLS = 80
TERM_ROWS = 173  # Approximately 19.5/9 * 80

def setup_virtual_display():
    display = Display(visible=0, size=(1200, 2600))
    display.start()
    return display

def create_tmux_session(session_name):
    subprocess.run(['tmux', 'new-session', '-d', '-s', session_name])
    subprocess.run(['tmux', 'set', '-g', 'status', 'off'])
    subprocess.run(['tmux', 'set', '-g', 'default-terminal', 'xterm-256color'])

def record_scene_1():
    """Initial setup and theme showcase"""
    commands = [
        ('nvim complex_service.py', 2),
        (':set termguicolors', 1),
        ('', 2),  # Pause to show theme
    ]
    return commands

def record_scene_2():
    """File navigation showcase"""
    commands = [
        ('<leader>tt', 2),  # Toggle NvimTree
        ('', 1),
        ('<leader>ff', 2),  # Telescope find files
        ('docker', 1),
        ('<CR>', 2),
        ('<leader>fg', 2),  # Telescope live grep
        ('service', 1),
        ('<CR>', 2),
    ]
    return commands

def record_scene_3():
    """LSP functionality"""
    commands = [
        ('nvim complex_service.py', 2),
        ('/UserMetrics', 1),
        ('gd', 2),  # Go to definition
        ('gr', 2),  # Find references
        ('K', 2),   # Hover documentation
        ('<space>rn', 1),  # Rename symbol
        ('EnhancedMetrics', 1),
        ('<CR>', 2),
    ]
    return commands

def record_scene_4():
    """Docker integration"""
    commands = [
        ('nvim docker-compose.yaml', 2),
        ('', 1),
        ('<leader>du', 2),  # Docker Compose Up
        ('', 3),  # Wait for Docker output
    ]
    return commands

def record_scene_5():
    """Debugging session"""
    commands = [
        ('nvim test_analytics.py', 2),
        ('<leader>dd', 2),  # Start debugger
        ('<leader>b', 1),   # Set breakpoint
        ('F10', 1),         # Step over
        ('F11', 1),         # Step into
        ('', 2),
    ]
    return commands

def main():
    scene_num = int(sys.argv[1])
    display = setup_virtual_display()
    
    session_name = f'scene-{scene_num}'
    create_tmux_session(session_name)
    
    # Select scene commands
    scene_commands = {
        1: record_scene_1,
        2: record_scene_2,
        3: record_scene_3,
        4: record_scene_4,
        5: record_scene_5,
    }[scene_num]()
    
    # Record the scene
    output_path = f'asciinema/scene-{scene_num}.cast'
    
    record_scene(
        commands=scene_commands,
        output_path=output_path,
        env={
            'TERM': 'xterm-256color',
            'COLUMNS': str(TERM_COLS),
            'LINES': str(TERM_ROWS),
        },
        tmux_session=session_name
    )
    
    display.stop()

if __name__ == '__main__':
    main()
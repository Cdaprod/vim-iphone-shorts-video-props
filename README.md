# Vim iPhone Shorts Video Props
> Automated Terminal Recordings for Viral Vim Content 🔥

This repository automatically generates asciinema recordings of advanced Vim usage, formatted for vertical social media content (9:19.5 aspect ratio).

## Quick Start

```bash
git clone https://github.com/Cdaprod/vim-iphone-shorts-video-props.git
cd vim-iphone-shorts-video-props
```

The recordings will automatically generate on push or via manual GitHub Actions trigger.

## How It Works

### Automated Recording Process

1. **GitHub Actions** automatically records Vim scenes on:
   - Every push to main
   - Manual workflow dispatch
   - Successfully recorded scenes are committed back to `/asciinema`

2. **Vertical Format**:
   - Terminal dimensions: 80x173 (9:19.5 ratio)
   - Perfect for shorts/reels
   - Optimized for mobile viewing

3. **Scene Sequence**:
   ```
   Scene 1: Setup & Theme
   Scene 2: File Navigation
   Scene 3: LSP Features
   Scene 4: Docker Integration
   Scene 5: Debug Session
   ```

## Usage

### Trigger Recordings

1. **Auto (on push)**:
   ```bash
   git push origin main
   ```

2. **Manual**:
   - Go to Actions tab
   - Click "Record Vim Scenes"
   - Select "Run workflow"

### View Recordings

```bash
# Play a specific scene
asciinema play asciinema/scene-1.cast

# Convert to gif (requires agg)
agg asciinema/scene-1.cast scene-1.gif
```

## Customization

### Add New Scene

1. Edit `.github/scripts/record_scene.py`:
   ```python
   SCENES = {
       6: [  # Your new scene
           ('your-command', delay_in_seconds),
           ...
       ],
   }
   ```

2. The workflow will automatically pick up new scenes.

### Modify Terminal Size

Edit in `.github/workflows/record-scenes.yml`:
```yaml
env:
  TERM_COLS: 80
  TERM_ROWS: 173  # Adjust for different aspect ratio
```

## Directory Structure

```
.
├── .github/
│   ├── workflows/
│   │   └── record-scenes.yml    # CI automation
│   ├── scripts/
│   │   └── record_scene.py      # Recording logic
│   └── asciinema/
│       └── config.json          # Terminal settings
├── asciinema/                   # Generated recordings
│   ├── scene-1.cast
│   ├── scene-2.cast
│   └── ...
└── init.lua                     # Your Neovim config
```

## Requirements

- GitHub Actions (included)
- Python 3.10+
- Neovim
- asciinema
- tmux

## Troubleshooting

### Common Issues

1. **Recording Fails**:
   ```bash
   # Check workflow logs in GitHub Actions
   # Verify terminal dimensions
   # Confirm all dependencies installed
   ```

2. **Playback Issues**:
   ```bash
   # Update asciinema
   asciinema --version
   
   # Verify cast file
   ls -l asciinema/*.cast
   ```

### Debug Mode

Add to workflow:
```yaml
- name: Debug Info
  run: |
    env | grep TERM
    tmux -V
    nvim --version
```

## Contributing

1. Fork the repository
2. Create feature branch
3. Add/modify scenes
4. Push changes
5. Create Pull Request

## License

MIT

---

**Note**: This project demonstrates automated terminal recording. For actual iPhone Vim usage, you'll need ShellFish and proper terminal setup.
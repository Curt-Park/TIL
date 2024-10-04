restic is a backup program that is fast, efficient and secure.
It supports the three major operating systems (Linux, macOS, Windows) and a few smaller ones (FreeBSD, OpenBSD).

## Installation
```bash
brew install restic
```

## Quick Start
```bash
export RESTIC_REPOSITORY=$HOME/restic-repo
export RESTIC_PASSWORD=some-strong-password
restic init

restic backup README.md
restic snapshots
restic restore --target restore-work your-snapshot-id
restic forget --keep-last 1 --prune
```

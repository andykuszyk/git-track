# git-track
A command line todo list and time tracker. 

## About
`git-track` uses ordinary git repositories to store todo lists and time (using a simple start/stop mechanism). This allows time tracking to be automated simply from the command line (e.g. integrated into normal window manager operations like locking the screen, powering off at the end of the day). This also means it's easy to share todo lists across multiple machines, by simply synching the git repositories.

## Installation
Simply copy the files in this directory into somewhere in your `$PATH`, e.g: `cp git-track* ~/.local/bin`.

## Usage
### Initialisation
Before use, `git track` must be initialised to use an existing git repository for storage. This can be done with the `git track init` command, e.g:

```sh
mkdir my-hours
cd my-hours
git init
cd ..
git track init $(pwd)/my-hours
```

### Creating TODO lists
`git track todo` will create an interactive commit from your most recent TODO commit, allowing you to maintain an updateable list.

### Time tracking
Simply start and stop time tracking with:

```sh
git track start
git track stop
```

### Reporting
Basic reporting of hours tracked is available using `git track report`.

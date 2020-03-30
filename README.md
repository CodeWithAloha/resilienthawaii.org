# Instructions

## Using Hugo Static Site Generator v0.69.0-DEV/extended darwin/amd64

## Commands to build hugo from source:

> git clone https://github.com/gohugoio/hugo.git
> cd hugo
> go install -tags extended

## Deploying site

Not using netlify's hooks because using latest Hugo source and need to figure
out how to specify the version of Hugo in Netlify's build process. For now, every push
to master will just publish the public/ folder (so just make sure to build it
locally before pushing)

hugo --minify --theme book

## Running locally

hugo server --theme book --disableFastRender

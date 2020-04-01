# ResilientHawaii.org

This is a [Hugo](https://github.com/gohugoio/hugo) site that is being updated
with the data the crowdsourced Google Document @ https://bit.ly/covid19hawaii.

The process is as follows:

- Create a shared Google document (start with what other cities have done like [NYC United Against Coronavirus](https://docs.google.com/document/d/18WYGoVlJuXYc3QFN1RABnARZlwDG3aLQsnNokl1KhZQ/edit) or [Resilient Hawaii](https://bit.ly/covid19hawaii))
- Send the document to the community at large
    - Recruit people in the community who make a lot of useful suggestions as editors (onboard them in a Slack group)
- Install a Google script to convert the Google document to Markdown (@sthapa will share)
- Run the script periodically to create a Markdown representation of the Google document
- Use Hugo + Netlify to update the content

## Using Hugo Static Site Generator v0.69.0-DEV/extended darwin/amd64

## Deploying site

We're not using netlify's hooks because using latest Hugo source and need to figure
out how to specify the version of Hugo in Netlify's build process. For now, every push
to master will just publish the public/ folder (so just make sure to build it
locally before pushing)

## Building via Docker

docker run --rm -it -v $(pwd):/src -v $(pwd)/public:/target klakegg/hugo:0.68.3-ext-alpine --theme book --minify

## Running server locally via Docker

docker run --rm -it -v $(pwd):/src -p 1313:1313 klakegg/hugo:0.68.3-ext-alpine server --theme book --disableFastRender

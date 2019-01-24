# Rabble rabble rabble

A very simple, anonymous, chat server.

I wrote this in < 3 hours for an interview project (roughly 80 minutes on the backend, 100 minutes on the frontend).

## Setup / Run

```sh
# To setup local DB
pipenv run python -c "import models; models.init_db()"
# To run app locally
./scripts/local-server.sh
```

## Backend

The backend is written in Python, using Flask for the web server and SQLAlchemy for database access. This is a tech stack I know and (mostly) love.

I spent probably too long (20 mins?) figuring out how to configure the Flask-SQLAlchemy plugin to work nicely. Historically, I've used SQLAlchemy directly and then managed sessions myself, but I didn't want to have to set up all the infrastructure to do that for a 3 hour interview project. Turns out, however, that the way that the Flask-SQLAlchemy plugin works lends itself to a circular import setup - the recommendation is instantiating the `SQLAlchemy` class with a Flask App as a constructor arg, but you also need to decorate your request handler methods with `@flask_app.route`, and to ensure that those request handler methods are available at import time for the app. In the end I got around this using `Blueprint`s and a `create_app` method, as per the `SQLAlchemy-Flask` tutorial, but this was a more of a timesink than I expected.

## Frontend

I am _not yet_ a frontend engineer, and that's probably clear when you look at the difference between the way the frontend and the backend are structured 😅 Everything is in `templates/index.html`. Seriously, _everything_. 

The frontend is CSS / JS / HTML5. No fancy frameworks, no transpilation - I only had 100 minutes for the frontend, I didn't want to spend ~30-60 installing toolchains and learning how to use a framework (these things _always_ take longer than you expect).

CSS: I'm using Twitter Bootstrap 4, which uses flexbox under the hood. There's no real naming scheme for the custom classes.

JS: I pulled in Jquery. I'm pretty aware that you [don't need it most of the time now](http://youmightnotneedjquery.com/), and, it's 30kB ?! But there's a line in the spec that says "make sure it works on a wide range of browsers", so I wanted to make sure that anything exotic / new was getting shimmed. This is definitely superstition-driven-development and I think also nullified by the fact that I used the `const var` keyword somewhere... but then [CanIUse](https://caniuse.com/#feat=const) says that `const` is pretty well supported nowadays, so maybe all of my knowledge about JS and compatibility is just wildly out of date.  

## Self-evaluation

I'm super happy with my prioritisation on this project. We've got something that works, in 3 hours, and has some idiosyncrasies, but nothing particularly deal-breaking (in my opinion). You can take a look at the git log to see the order in which I built things.

If I had more time, here's probably the next few things I'd do, in order:

- Right now we're rebuilding the entire message history in the DOM every 5 seconds, and then scrolling to the end. This means it's not possible to scroll back through history, because after 5 seconds, you'll get pushed back down to the bottom. Instead, I'd fix this to only load what's new/changed (the API supports this already, there's a `since` parameter on the GET `/api/messages` endpoint).
  - _Probably_ I wouldn't scroll to the bottom automatically if you're not already at the bottom when new messages come in, but this sounds like it's fiddly and hard to get right. In situations like this, I'd have some UX affordance to show that new messages have come in.
  - Paginating historical messages / not loading _all_ historical messages on page load also sounds valuable, and is related to this.
- Persist username in a cookie or `localStorage` (but, if I recall correctly, `localStorage` only works on HTTPS so this would be a pain to setup for local dev environments). That way, users can retain the same identity across multiple page reloads.
- Send session IDs to the server instead of just "username". Right now, anyone can impersonate anyone, and giving people that level of trust on a completely anonymous app seems like a real bad thing. I'd love to create UX affordances to differentiate between different people using the same username to limit one avenue of abuse.
- Look into some kind of JS rendering framework. Wow, I understand why Angular / React / Vue and friends evolved now! It's awful doing this stuff by hand. In retrospect, hacking things together still feels like the right thing to have done in the short term, but long-term development using loosely-ordered JS is _not_ particularly sustainable.

Depending on how polished you want to make this, there's some other stuff that probably should be done:
- Websockets would be nice, rather than just refreshing messages content every 5 seconds
- Definitely need it to make a 'bloop' sound whenever you get a new message
- Work out if it's possible to make this work for users without Javascript. It's kinda nasty that the content is only accessible over JS, and you can't post new messages without it. This is very difficult to prioritise though - there's basically two directions you can take with JS, and that's "all in" or "only enhancements", and this project is definitely more of an "all in" one, given the UX / project specs.
- The ability to actually set your username, rather than just allocating you a random identity on load, would probably be nice :) But, there's something also kinda magical about being able to switch to new random identities at will:

!["i know, all you have to do is refresh the page and suddenly, your identity changes"](https://i.imgur.com/jFjFFvc.png) 

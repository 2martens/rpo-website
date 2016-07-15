# RPO website

This repository contains the code and the design documents for
the RPO website. RPO stands for "Rahmenprüfungsordnung" which contains university
wide exam regulations. There is no ideal translation into English but the
abbreviation RPO is very well pronouncable in English. Therefore it will
be used everywhere instead of the long version.

## Goal/Mission of the website

The website shall be the central hub for all things RPO. Whenever you
have a question about the RPO, the website will be there to help you out.
It will contain all the information and will list arguments why the RPO
is something good and useful.

## Access levels

### Public

The public facing parts of the website will be the first implemented
and most widely used. They contain mostly information. These things are public:

- progress meter (shows the steps necessary for formal approval in the Academic 
  Senate and at which point in the process we currently are)
- public statements of all sorts (faculty and department statements but also 
  additional statements)
- fact checking of arguments against RPO
- arguments in favour of RPO based on evidence
- information on how to participate in the process
- list of supporters (split by status group and university)
- list of coordinating people (responsible for the website and the campaign)

In addition to this public information you can also show your support by
providing this information:

- your name
- your email
- your status group
- your university
- your faculty
- your course of study (e.g. Informatics BSc.)
- optional field with additional info (e.g. member of parliament)
- optional field with referrer ID (if activist part is implemented)

You can also do this anonymously. In this case your name won't be displayed
publicly. Your email will not be displayed publicly in any case. It is only
used to verify your support (effectively preventing people from fake adding
other people to this list).

### Activist-only

In addition to the public information and actions there will things visible
only to pledged supporters. This part of the website will be developed after
the public part and may be scrapped. If it is implemented the following things
will be found here.

First of all: Once you have shown your support (passive supporter), a hidden
account will be created for you. If you so choose you can up your support to
active by pledging to campaign for the RPO. In that case you will get an
active account. You can login by using your email and a password generated for
you. This PW should be changed ASAP after initial login. When becoming
an active member you accept that the coordinating people can send you
emails to remind you about upcoming events and other useful information.

Once logged in you will get access to strategic tips on how to argue best
for the RPO including typical arguments against the RPO and how to debunk
them. Furthermore you will see a list of planned events and what you can do
to support them. Moreover you are able to announce events that will be made
available to everyone to see once a coordinating person has reached out to
you to discuss what these events are about.

Plus you can pledge to convince your fellow students. For this case every
activist will get a unique referrer ID. If someone mentions this ID when
showing support the counter of convinced people for that referring activist
is increased by 1. If someone mentioned your ID when showing support and becomes 
an active supporter afterwards your counter of converted people is increased
by 1. It is one thing to get someone to passively support the RPO but another
to make them actively campaign for it. At the end of the campaign both the
people who convinced most and the people who converted most will be announced
if they so choose. This should work as a small incentive to convince as many 
people as possible.

### Coordinaters

This access levels is basically the admin level and will be the place
to edit the information visible in the frontend and fetch the list
of all supporters both passive and active.

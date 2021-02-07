# Serverless Calendar Journal

A journal management function.

## Overview

A calendar journal is useful for recording outcomes of past events and keeping records of achievements. A journal
consists of a series of entries that record descriptive information and any related participants, attachments,
comments, etc.

A journal might be used to record meeting minutes (absentees, discussion points, actions, etc.), track activities
and outcomes of actions, or as a personal diary or microblogging platform.

### Revisions

A journal entry may consist of multiple revisions representing changes to the recorded details. Each revision is
stored as a separate record in the database. The unique identifiers making up the composite key include:

* UID - Unique identifier for the journal entry (shared by all revisions of an entry)
* Sequence Number - Incremental revision identifier (indicates new revision of an entry)
* Recurrence ID - A timestamp identifier for specific instances of a recurring journal entry

### Attachments

A journal entry may refer to one or more attachments via an external link (URL) or an inline base64 encoded binary.

### Comments

One or more comments can be associated with a journal entry, which are defined via inline text or an external
reference (URL).

### Contacts

Multiple contacts may also be associated with a journal entry. Contact information may be define as inline text
and/or an external reference (URI).

### Categories

Text-based labels or categories may be associated with a journal entry.

### Related

Related calendar entries, journals or tasks may also be recorded against a journal entry. An example of this may be
when a journal entry represents recorded minutes for a meeting.

### Classification

Journal entries may be classified as public, private or confidential, and may be used to control access and controls
applied to a journal entry.


## Specification

### DynamoDB

| PK                                            | SK                  | Name        | Date       | Summary           | Description                | Classification | URL                                  |
|-----------------------------------------------|---------------------|-------------|------------|-------------------|----------------------------|----------------|--------------------------------------|
| ENTRY# `<uid>` # `<sequenceno>` # `<recurid>` | #METADATA#`<uid>`.. | Jan 01 2021 | 2020-01-01 | First day of 2021 | Relaxing start to the year | PUBLIC         | -                                    |
| ENTRY# `<uid>` # `<sequenceno>` # `<recurid>` | CATEGORY#my-journal | My Journal  |            |                   |                            |                |                                      |
| ENTRY# `<uid>` # `<sequenceno>` # `<recurid>` | ATTACH#1            | -           | -          | -                 | -                          |                | https://photos.example.com/relax.png |
| ENTRY# `<uid>` # `<sequenceno>` # `<recurid>` | CONTACT#1           | John Doe    | -          | -                 | -                          |                | johnd@example.com                    |

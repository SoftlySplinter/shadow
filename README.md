Shadow
======

A (possibly changing) rougelike stealth game.


Mechanics
---------

Here's some random thoughts I've had which I might be able to use:

###Entity Manager
Has a hold of all game entities, handles each game tick, etc.

###Entity
A game entity, subtypes include:

* Actor - A moving entity with some for of sentience
    * Player - The actor controlled by a human being
* Tile - A non-moving entity which forms part of the scene

####Methods
* tick():void
* passable():boolean


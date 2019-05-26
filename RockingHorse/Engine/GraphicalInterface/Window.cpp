// Window.cpp
//
// base class for game windows
//
// 5-24-2019 by arn

#include "Window.hpp"

Window::Window() {
	name = "Rocking Horse";
	gameWidth = 1080;
	gameHeight = 720;
	bpPix = 32;

	// Create the window of the application
	sf::VideoMode mode = sf::VideoMode(gameWidth, gameHeight, bpPix);
	// mode = mode.getFullscreenModes()[0];
	sf::RenderWindow mainWindow = sf::RenderWindow(mode, name, sf::Style::Titlebar | sf::Style::Close);
	mainWindow.setFramerateLimit(30); // call it once, after creating the window

	sf::View mainView = mainWindow.getView();
	sf::View viewLeft(sf::FloatRect(0.0f, 0.0f, gameWidth / 2.0f, gameHeight / 2.0f));
	viewLeft.setViewport(sf::FloatRect(0, 0, 0.5, 0.5));

	sf::View viewRight(sf::FloatRect(0.0f, 0.0f, gameWidth / 2.0f, gameHeight / 2.0f));
	viewRight.setViewport(sf::FloatRect(0.5, 0, 0.5, 0.5));

	sf::View viewBottom(sf::FloatRect(0.0f, 0.0f, gameWidth + 0.0f, gameHeight / 2.0f));
	viewBottom.setViewport(sf::FloatRect(0, .75, 1, 0.25));


	sf::Font font;
	// load and set font
	font.loadFromFile("arial.ttf");

	/*
	sf::Text text("You are standing in the library.\n\n"
		"The room is decently lit, well enough to read in at the very least.\n\n"
		"You find yourself surrounded by bookshelves, twice as tall as you, \n"
		"and a statue in the center.\n\n"
		"Most of the shelves are filled to the brim with books, of varying \n"
		"states of upkeep.\n\n"
		"At the opposite end of the room is a blackwood desk, with a faded \n"
		"silver reading lamp, currently shining upon a leatherbound book.\n\n"
		, font);
	*/

	sf::Text text("You are standing in the library.\n", font);

	std::string player_cmd = "";
	sf::Text cmd_text(player_cmd, font);

	// set the character size
	text.setCharacterSize(20); // in pixels, not points!
	// set the color
	text.setFillColor(sf::Color::White);
	// set the text style
	// text.setStyle(sf::Text::Bold);

}

sf::RenderWindow Window::getMainWindow() {
	return mainWindow;
}

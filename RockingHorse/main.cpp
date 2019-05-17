// main.cpp

#include <stdlib.h>
#include <iostream>
#include <string>
#include <SFML/Graphics.hpp>

int main()
{
	// render window
	sf::RenderWindow window(sf::VideoMode(800, 600), "TEST WINDOW");
	window.setFramerateLimit(30); // call it once, after creating the window

	// viewports
	sf::View standard = window.getView();

	sf::View viewLeft(sf::FloatRect(0.0f, 0.0f, window.getSize().x / 2.0f, window.getSize().y / 1.5f));
	viewLeft.setViewport(sf::FloatRect(0, 0, 0.5, 0.75));

	sf::View viewRight(sf::FloatRect(0.0f, 0.0f, window.getSize().x / 2.0f, window.getSize().y / 1.5f));
	viewRight.setViewport(sf::FloatRect(0.5, 0, 0.5, 0.75));

	sf::View viewBottom(sf::FloatRect(0.0f, 0.0f, window.getSize().x + 0.0f, window.getSize().y / 2.5f));
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

	while (window.isOpen())
	{
		// GAME LOOP
		sf::Event event;
		
		while (window.pollEvent(event))
		{
			switch (event.type) {
				// Close Window
				case sf::Event::Closed:
					window.close();
					break;

				case sf::Event::TextEntered:
					if (event.text.unicode < 128) {
						player_cmd += static_cast<char>(event.text.unicode);
						std::cout << "ASCII character typed: " << event.text.unicode << std::endl;

						if (event.text.unicode == 8) {
							player_cmd.pop_back();
							player_cmd.pop_back();
						}
					}

				case sf::Event::KeyPressed:
					if (event.key.code == sf::Keyboard::Escape) {
						window.close();
						break;
					}

				default:
					break;
			}
		}

		// start draw pipeline
		window.clear(sf::Color::Black);

		window.setView(viewLeft);
		window.draw(text);

		window.setView(viewRight);
		window.draw(text);

		window.setView(viewBottom);
		cmd_text.setString(player_cmd);
		window.draw(cmd_text);
		
		window.display();
		// end draw pipeline
	}

	return EXIT_SUCCESS;
}
// main.cpp

#include <stdlib.h>
#include <iostream>
#include <string>

#include "GraphicalInterface/Window.hpp"

int main()
{
	Window gameWindow = Window();

	while (gameWindow.indow.isOpen())
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
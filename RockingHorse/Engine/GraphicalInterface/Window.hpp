// Window.hpp
//
// base class for game windows
//
// 5-24-2019 by arn

#pragma once

#ifndef WINDOW_H
#define WINDOW_H

#include "string.h"

#include <SFML/Graphics.hpp>

class Window {
private:

public:
	Window();

	std::string name;
	int gameWidth;
	int gameHeight;
	int bpPix;

	sf::VideoMode mode;
	sf::RenderWindow mainWindow;

	sf::View mainView;

	sf::RenderWindow getMainWindow();

};

#endif
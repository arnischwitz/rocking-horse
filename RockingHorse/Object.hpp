// Object.hpp
//
// base oop class header for in game actors
//
// 5-8-2019 by arn

#pragma once

#ifndef OBJECT_H
#define OBJECT_H

#include "string"

class Object {
private:
	// Object m_owner;
	std::string m_description;

public:
	Object();

	std::string getDescription()
	{
		return m_description;
	}
};

#endif
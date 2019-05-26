// Interactable.h
//
// base class for interactable objects
//
// 5-8-2019 by arn

#pragma once

#ifndef INTERACTABLE_H
#define INTERACTABLE_H

#include "Object.h"

#include "string"

class Interactable: public Object {
private:
	// Object m_owner;
	std::string m_description;

public:
	Interactable();

	std::string getDescription()
	{
		return m_description;
	}
};

#endif
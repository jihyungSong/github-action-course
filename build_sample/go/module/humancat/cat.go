package main

type Cat struct {
	name   string
	status string
}

func (c Cat) get_name() string {
	return c.name
}

func (c Cat) set_name(name string) {
	c.name = name
}

func (c Cat) get_status() string {
	return c.status
}

func (c Cat) set_status(status string) {
	c.status = status
}

func (c Cat) meow() string {
	return "Meow"
}

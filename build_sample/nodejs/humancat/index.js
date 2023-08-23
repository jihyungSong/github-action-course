var cat = require('./lib/cat')
var human = require('./lib/human')

class Humancat {
  constructor(human_name, cat_name){
     this.human = new human(human_name);
     this.cat = new cat(cat_name);
  }
}

module.exports = {Humancat};
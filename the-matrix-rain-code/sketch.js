var streams = [];
var symbolSize = 15;

function setup() {
	createCanvas(windowWidth, windowHeight);

	var x = 0;
	for (var i = 0; i <= width / symbolSize; i++) {
		var y = random(0, height);
		var stream = new Stream(x);
		stream.generateSymbols(x, y);
		streams.push(stream);
		x += symbolSize + 10;
	}
	textSize(symbolSize);
}

function draw() {
	background(0, 150);
	//translate(mouseX, mouseY);
	streams.forEach(function(stream) {
		stream.render();
	});
}

//************************************
function Symbol(x, y, speed, first, alpha) {
	this.x = x;
	this.y = y;
	this.value;
	this.speed = speed;
	this.switchInterval = round(random(20, 100));
	this.first = first;
	this.alpha = alpha;

	this.setToRandomSymbol = function() {
		if (frameCount % this.switchInterval == 0) {
			this.value = String.fromCharCode(
				0x30A0 + round(random(0, 96))
			);
		}
	}

	this.rain = function(sp) {
		if(this.y >= height) {
			this.y = 0
		};
		this.y += sp//map (mouseY, 0, height, 1, this.speed);//this.speed;
		//this.y = (this.y >= height) ? 0 : this.y += this.speed; //This is a short version of the above.
	}
}

//*************************************
function Stream(x) {
	this.symbols = [];
	this.totalSymbols = round(random(5, 30));
	this.speed = random(5, 20);
	this.x = x;

	this.generateSymbols = function(x, y) {
		var first = round(random(0,4)) == 1;
		var alpha = 200;

		for (var i = 0; i <= this.totalSymbols; i++) {
			symbol = new Symbol(x, y, this.speed, first, alpha);
			symbol.setToRandomSymbol();
			this.symbols.push(symbol);
			y -= symbolSize + 2;
			first = false;
			alpha = map(i, 0, this.totalSymbols, 200, 100);
		}
	}

	this.render = function() {
		var sp = map (mouseY, 0, height, 1, this.speed);
		var highlight = this.x + symbolSize / 2 >= mouseX && mouseX >= this.x - symbolSize / 2;
		fill(254,226,62);

		// Changes ** introduced to keep the symbols at the same distance.
		var temp = this.symbols[0].y + sp; //If use .rain(sp) do not use this**
		if (temp > height) {temp -= height}; //**
		this.symbols.forEach(function(symbol) {
			if (!highlight) {
				if (symbol.first) {
					fill(255,17,0, symbol.alpha);
				} else {
					fill(0, 255, 70, symbol.alpha);
				};
			}
			symbol.y = temp; //**
			text(symbol.value, symbol.x, symbol.y);
			temp -= symbolSize + 2; //**
			if (temp < 0) {temp += height}; //**
			//symbol.rain(sp);
			symbol.setToRandomSymbol();
		})
	}
}

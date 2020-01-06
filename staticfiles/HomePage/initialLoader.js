var canv = document.createElement('canvas');
// var logo = document.getElementById('logo');
var Space = (function () {
    function Space() {
        this.canvas = canv;
        this.ctx = this.canvas.getContext('2d');
        this.canvas.style.position="absolute";
        this.canvas.style.top="0";
        this.canvas.style.zIndex="-100000";
//		this.canvas.style.height="100vh";
//		this.canvas.style.width="100vw";
        this.particles = [];
        this.ratio = window.innerHeight < 400 ? 1 : 1;
        if(window.innerWidth<800){
            this.r = 120;
        }else{
            this.r = 180;
        }
        // this.r = 550;
        this.counter = 0;
    }
    Space.prototype.init = function () {
        this.createElement();
        this.loop();
    };
    Space.prototype.createElement = function () {
        var scale = this.ratio;
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
        this.canvas.style.width = '100%';
        this.canvas.style.height = '105%';
        this.canvas.style.marginTop='-5px';
        this.canvas.style.background = 'rgb(0, 0, 0)';
        this.ctx.transform(scale, 0, 0, -scale, this.canvas.width / 2, this.canvas.height / 2);
        // this.ctx.drawImage(logo, this.canvas.width / 2, this.canvas.height / 2);
        document.body.appendChild(this.canvas);
        for (var i = 0; i < 450; i++) {
            this.createParticle();
        }
    };
    Space.prototype.createParticle = function () {
        this.particles.push({
            color: Math.random() > 0.5 ? "rgba(255, 255, 255, 1)" : "rgba(255, 255, 255, 0.4)",
            radius: Math.random() * 5,
            x: Math.cos(Math.random() * 7 + Math.PI) * this.r,
            y: Math.sin(Math.random() * 7 + Math.PI) * this.r,
            ring: Math.random() * this.r * 3,
            move: ((Math.random() * 4) + 1) / 500,
            random: Math.random() * 7
        });
    };
    Space.prototype.moveParticle = function (p) {
        p.ring = Math.max(p.ring - 1, this.r);
        p.random += p.move;
        p.x = Math.cos(p.random + Math.PI) * p.ring;
        p.y = Math.sin(p.random + Math.PI) * p.ring;
    };
    Space.prototype.resetParticle = function (p) {
        p.ring = Math.random() * this.r * 3;
        p.radius = Math.random() * 5;
    };
    Space.prototype.disappear = function (p) {
        if (p.radius < 0.8) {
            this.resetParticle(p);
        }
        p.radius *= 0.994;
    };
    Space.prototype.draw = function (p) {
        this.ctx.beginPath();
        this.ctx.fillStyle = p.color;
        this.ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        this.ctx.fill();
    };
    Space.prototype.loop = function () {
        this.ctx.clearRect(-this.canvas.width , -this.canvas.height, this.canvas.width * 2, this.canvas.height * 2);
        if (this.counter < this.particles.length) {
            this.counter++;
        }
        //this.ctx.shadowBlur = 20;
        //this.ctx.shadowColor = "#fff";
        for (var i = 0; i < this.counter; i++) {
            this.disappear(this.particles[i]);
            this.moveParticle(this.particles[i]);
            this.draw(this.particles[i]);
        }
        requestAnimationFrame(this.loop.bind(this));
    };
    return Space;
})();

window.addEventListener("resize",function(){
	var space = new Space();
    space.init();
});
window.onload = function () {
    var space = new Space();
    space.init();
};
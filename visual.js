String.prototype.format = function(args) {
    let result = this;
    if (arguments.length > 0) {
        if (arguments.length === 1 && typeof (args) === "object") {
            for (let key in args) {
                if(args[key]!==undefined){
                    let reg = new RegExp("({" + key + "})", "g");
                    result = result.replace(reg, args[key]);
                }
            }
        }
        else {
            for (let i = 0; i < arguments.length; i++) {
                if (arguments[i] !== undefined) {
                    let reg= new RegExp("({)" + i + "(})", "g");
                    result = result.replace(reg, arguments[i]);
                }
            }
        }
    }
    return result;
};

let left_stack = [];
let right_stack = [];


function GCD(d, varphi){
        if(d===0){
            right_stack.push([varphi, 0, 1]);
            return [varphi, 0, 1]
        }
        else{
            left_stack.push([varphi%d, d]);
            let result = GCD(varphi%d, d);
            let g = result[0];
            let x = result[1];
            let y = result[2];
            right_stack.push([g,y-Math.floor(varphi/d)*x,x]);
            return [g, y-Math.floor(varphi/d)*x,x]
        }
}



function animation(result){
    let playground = $('#playground');
    for(let i=0;i<left_stack.length;i++){
       let array = left_stack[i];
       let new_obj = $('#left_obj').clone();
       playground.append(new_obj);
       new_obj.attr('id', i);
       new_obj.attr('new',1);
       new_obj.text("d={0}\tφ={1}".format(array[0], array[1]));
       setTimeout(function(){new_obj.show();snabbt(new_obj,{position: [0, 500-i*150, 0],rotation: [0, 0, 0],easing: 'ease'})}, 1500*i);
    }
    for(let i=0;i<right_stack.length;i++){
       let array = right_stack[i];
       let new_obj = $('#right_obj').clone();
       new_obj.attr('new',1);
       playground.append(new_obj);

       new_obj.text("g={0}\tx={1}\ty={2}".format(array[0], array[1], array[2]));
       setTimeout(function(){new_obj.show();snabbt(new_obj,{position: [0, 200+(i+1)*50, 0],rotation: [0, 0, 0],easing: 'ease'})}, 1500*i+left_stack.length*1500);
    }
    let bottom = $('#btm_obj').clone();
    bottom.text('Result e = '+result[1]);
    playground.append(bottom);
    bottom.attr('new',1);
    setTimeout(function(){bottom.fadeIn(2000);},(left_stack.length+right_stack.length)*1500)
}


$("#start").click(function(){
    let divs = $("[new]");
    divs.remove();
    let d = parseInt($("#d").val());
    let fa = parseInt($('#fa').val());
    if(d && fa){
        left_stack = [[d,fa]];
        right_stack = [];
        let result = GCD(d, fa);
        animation(result);
    }
});


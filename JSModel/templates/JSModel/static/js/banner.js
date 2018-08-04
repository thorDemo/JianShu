window.onload = function () {
    let start = setInterval(autoPlay, 2000);
    let index = 0;
    function autoPlay() {
        if(index>2){
            index=0;
        }
        changeImage(index);
        index++;
    }
    function changeImage() {
        let show = $('div.active.item');
        show.removeClass('active');
        jQuery($('div.item')[index]).addClass('active');
        let slide = $('ol.carousel-indicators li.active');
        slide.removeClass('active'); 
        jQuery($('ol.carousel-indicators li')[index]).addClass('active');
    }
    let mouse = $('.item.active');
    mouse.mouseover(function () {
        console.log('take in ');
        clearInterval(start)
    });
    mouse.mouseout(function(){
        console.log('take out ');
        start = setInterval(autoPlay, 2000);
    });
};
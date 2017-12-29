
// 全局变量:在函数外声明;函数内不使用var
global_var = 'global_var';
// 判断类型 typeof 返回的是字符串，有六种可能："number"、"string"、"boolean"、"object"、"function"、"undefined"
console.log(typeof (global_var) == 'string');
console.log(typeof (undefined_var) == 'undefined');




$(function () {
    // 获取一类元素中被点击的
    // http://blog.csdn.net/itdada/article/details/27202513
    $("p.click_e").click(function () {
        //this表示当前被点击元素，但是此时我们当做dom对象
        alert(this.innerHTML);
        //$(this) 表示当前被点击元素，但是此时我们当做jquery对象
        alert($(this).html());
    });
    // 获取属性，内容
    $("#acquire_id_name_value").click(function () {
        var id = $(this).attr('id');
        var val = $(this).attr('value');
        var name = $(this).html();
        console.log(id, val, name);
    });
    // 动态生成元素
    ul_num = 0;
    $("#dynamic_e_click").click(function () {
        //console.log($('#dynamic_e_click + ul ').html() + '1');
        $('#dynamic_e_click + ul').append("<li idx=" + ul_num + ">new element:" + ul_num + "</li>");
    });
    // 动态元素添加事件
    $("#dynamic_e_click ul").on('click', 'li', function () {
        console.log($(this).html());
    });
    // 动态生成div
    var creatediv = function () {
        var parentdiv = $('<div></div>');        //创建一个父div
        parentdiv.attr('id', 'parent');        //给父div设置id
        parentdiv.addclass('parentdiv');    //添加css样式
        var childdiv = $('<div></div>');        //创建一个子div
        childdiv.attr('id', 'child');            //给子div设置id
        childdiv.addclass('childdiv');    //添加css样式
        childdiv.appendto(parentdiv);        //将子div添加到父div中
        parentdiv.appendto('body');            //将父div添加到body中
    }
    // 获取鼠标位置
    $("#mouse_location").click(function (e) {

        var offset = $(this).offset();
        var relativeX = (e.pageX - offset.left);
        var relativeY = (e.pageY - offset.top);

        alert("X: " + relativeX + "  Y: " + relativeY);

    });
    //功能：画实心圆
    //参数：圆心坐标，半径，精确度，背景颜色
    function SolidCircle(cx, cy, r, p, color) {
        var s = 1 / (r / p);
        for (var i = 0; i < Math.PI * 2; i += s) {
            var div = document.createElement("div");
            div.style.position = "absolute";
            div.style.left = Math.sin(i) * r + cx + "px";
            div.style.top = Math.cos(i) * r + cy + "px";
            div.style.width = p + "px";
            div.style.height = p + "px";
            div.style.backgroundColor = color;
            document.body.appendChild(div);
        }
    }
    SolidCircle(450, 200, 20, 5, "green");
    $("#send_ajax").click(function() {
        data = new Object();
        data.a = 'haha';
        data.b = new Array();
        $.ajax({
            type: "POST",
            url: "your_url",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(data),
            dataType: "json",
            success: function (message) {
                if (message > 0) {
                    alert("请求已提交！我们会尽快与您取得联系");
                }
            },
            error: function (message) {
                alert("提交数据失败！");
            }
        });
    }); 
});
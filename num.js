function init() {
    var num = document.getElementsByName('btn');
    var text_num = document.getElementById('div2');
    var text_num1,fuh;
    for (i = 0; i < num.length; i++) {
        num[i].onclick = function () {

            //判断按钮是数字
            if (!isNaN(this.value))
                //是数字,判断第一个是不是0
                if (text_num.value === '0'|| text_num.value === '除数不能为0') {
                    text_num.value = this.value;
                }
                else {
                    text_num.value += this.value;
                }
            else {
                if (text_num.value === '除数不能为0'){

                }else{
                    switch (this.value) {
                    case 'Enter':
                        switch (fuh){
                            case '+':
                                text_num.value = text_num1 + Number(text_num.value);
                                break;
                            case '-':
                                text_num.value = text_num1 - Number(text_num.value);
                                break;
                            case '*':
                                text_num.value = text_num1 * Number(text_num.value);
                                break;
                            case '/':
                                if (text_num.value ==='0'){
                                    text_num.value = '除数不能为0'
                                }else {
                                    text_num.value = text_num1 / Number(text_num.value);
                                }
                                break;
                            case 'Num':
                                text_num.value = 0;
                                break;
                        }
                        break;
                    default:
                        text_num1 = Number(text_num.value);
                        text_num.value = '0';
                        fuh = this.value
                        break;
                }
                }

            }
        }
    }
}


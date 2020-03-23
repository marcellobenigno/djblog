$(".alert").show().delay(4000).fadeOut();


$(function () {
    var MaskBehavior = function (val) {
        return val.replace(/\D/g, '').length === 11 ? '(00)00000-0000' : '(00)0000-00009';
    };
    var spOptions = {
        onKeyPress: function (val, e, field, options) {
            field.mask(MaskBehavior.apply({}, arguments), options);
        }
    };
    $('#id_phone').mask(MaskBehavior, spOptions);

});
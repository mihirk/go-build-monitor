(function (e) {
    var t = function (t, n) {
        return e(t).find(".cssConsoleDisplay span").removeClass("selected"), clearInterval(t.cursor), t.cursor_position != e(t).find(".cssConsoleDisplay span").length ? (e(t).find(".cssConsoleCursor").css({visibility: "hidden"}), e(t).find(".cssConsoleDisplay span").eq(t.cursor_position).addClass("selected"), t.cursor = window.setInterval(function () {
            e(t).find(".cssConsoleDisplay span").eq(t.cursor_position).hasClass("selected") ? e(t).find(".cssConsoleDisplay span").eq(t.cursor_position).removeClass("selected") : e(t).find(".cssConsoleDisplay span").eq(t.cursor_position).addClass("selected")
        }, n)) : (e(t).find(".cssConsoleCursor").css({visibility: "visible"}), t.cursor = window.setInterval(function () {
            e(t).find(".cssConsoleCursor").css("visibility") === "visible" ? e(t).find(".cssConsoleCursor").css({visibility: "hidden"}) : e(t).find(".cssConsoleCursor").css({visibility: "visible"})
        }, n)), t
    }, n = {init: function (n) {
        var r = e.extend({type: "text", inputId: null, inputName: null, inputValue: null, blinkingInterval: 500, charLimit: 0, preventEnter: !0, onEnter: function () {
        }}, n);
        return this.each(function () {
            var n = this, i = e(this);
            n.cursor, n.cursor_position = 0, n.inputVal = "", n.blinkingInterval = r.blinkingInterval, i.addClass("cssConsole"), i.append('<span class="cssConsoleDisplay"></span>'), i.append('<div class="cssConsoleCursor"></div>'), i.append('<input class="cssConsoleInput" type="' + r.type + '" />'), r.inputId && i.find(".cssConsoleInput").attr("id", r.inputId), r.inputName && i.find(".cssConsoleInput").attr("name", r.inputName);
            if (r.inputValue) {
                r.charLimit > 0 && r.charLimit < r.inputValue.length && (r.inputValue = r.inputValue.substring(0, r.charLimit)), n.cursor_position = r.inputValue.length;
                for (var s = 0; s < r.inputValue.length; s++)i.find(".cssConsoleDisplay").append("<span>" + r.inputValue.charAt(s) + "</span>");
                i.find(".cssConsoleInput").val(r.inputValue), n.inputVal = r.inputValue
            }
            return i.on("click", function () {
                i.find(".cssConsoleInput").focus(), t(n, r.blinkingInterval)
            }), i.find(".cssConsoleInput").on("focus", function () {
                t(n, r.blinkingInterval)
            }), i.find(".cssConsoleInput").on("blur", function () {
                clearInterval(n.cursor), n.cursor_position != i.find(".cssConsoleDisplay span").length ? i.find(".cssConsoleDisplay span").removeClass("selected") : i.find(".cssConsoleCursor").css({visibility: "hidden"})
            }), i.find(".cssConsoleInput").on("keydown", function (e) {
                e.which == 8 ? n.cursor_position > 0 && (i.find(".cssConsoleDisplay span").eq(n.cursor_position - 1).remove(), n.inputVal = n.inputVal.slice(0, n.cursor_position - 1) + n.inputVal.slice(n.cursor_position, n.inputVal.length), n.cursor_position--) : e.which == 13 ? (r.preventEnter && e.preventDefault(), r.onEnter()) : e.which == 46 ? (n.cursor_position < i.find(".cssConsoleDisplay span").length && i.find(".cssConsoleDisplay span").eq(n.cursor_position).remove(), n.inputVal = n.inputVal.slice(0, n.cursor_position) + n.inputVal.slice(n.cursor_position + 1, n.inputVal.length)) : e.which == 35 ? n.cursor_position = i.find(".cssConsoleDisplay span").length : e.which == 36 ? n.cursor_position = 0 : e.which == 37 ? n.cursor_position > 0 && n.cursor_position-- : e.which == 39 && n.cursor_position < i.find(".cssConsoleDisplay span").length && n.cursor_position++, i.find(".cssConsoleInput").is(":focus") && t(n, r.blinkingInterval)
            }), i.find(".cssConsoleInput").on("keyup", function (e) {
                if (e.which != 8 && e.which != 46 && n.inputVal != i.find(".cssConsoleInput").val()) {
                    i.find(".cssConsoleDisplay").empty();
                    if (n.inputVal.length == i.find(".cssConsoleInput").val().length)for (var s = 0; s < i.find(".cssConsoleInput").val().length; s++)r.type == "password" ? i.find(".cssConsoleDisplay").append("<span>*</span>") : i.find(".cssConsoleDisplay").append("<span>" + i.find(".cssConsoleInput").val().charAt(s) + "</span>"); else {
                        r.charLimit > 0 && r.charLimit < i.find(".cssConsoleInput").val().length && i.find(".cssConsoleInput").val(i.find(".cssConsoleInput").val().substring(0, r.charLimit));
                        for (var s = 0; s < i.find(".cssConsoleInput").val().length; s++)r.type == "password" ? i.find(".cssConsoleDisplay").append("<span>*</span>") : i.find(".cssConsoleDisplay").append("<span>" + i.find(".cssConsoleInput").val().charAt(s) + "</span>");
                        n.cursor_position = n.cursor_position + i.find(".cssConsoleInput").val().length - n.inputVal.length
                    }
                    n.inputVal = i.find(".cssConsoleInput").val(), t(n, r.blinkingInterval)
                }
            }), this
        })
    }, destroy: function () {
        return this.each(function () {
            var t = this, n = e(this);
            return t.cursor_position = 0, clearInterval(t.cursor), n.find(".cssConsoleInput").val(""), n.empty(), n.removeClass("cssConsole"), this
        })
    }, reset: function () {
        return this.each(function () {
            var n = this, r = e(this);
            return n.cursor_position = 0, n.cursor_position != r.find(".cssConsoleDisplay span").length && r.find(".cssConsoleDisplay span").removeClass("selected"), r.find(".cssConsoleInput").val(""), n.inputVal = "", r.find(".cssConsoleInput").is(":focus") ? t(r, n.blinkingInterval) : (clearInterval(n.cursor), r.find(".cssConsoleCursor").css({visibility: "hidden"})), r.find(".cssConsoleDisplay").empty(), this
        })
    }};
    e.fn.cssConsole = function (t) {
        if (n[t])return n[t].apply(this, Array.prototype.slice.call(arguments, 1));
        if (typeof t == "object" || !t)return n.init.apply(this, arguments);
        e.error("Method " + t + " does not exist on jQuery.cssConsole")
    }
})(jQuery)
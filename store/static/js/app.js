let cart = JSON.parse(localStorage.getItem('cart')) || [];

function addToCart(bookId, bookName, price) {
    // ✅ أولاً: أضف للسلة المحلية (localStorage)
    cart.push({ name: bookName, price: price });
    localStorage.setItem('cart', JSON.stringify(cart));

    // ✅ ثانياً: أرسل للسيرفر لتخزينه في قاعدة بيانات Django
    fetch('/add-to-cart/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: `book_id=${bookId}&quantity=1`
    })
    .then(res => res.json())
    .then(data => {
        if (data.status === 'ok') {
            alert(`${bookName} تمت إضافته للسلة بنجاح! ✅`);
        } else {
            alert('حدث خطأ أثناء الإضافة للسلة ');
        }
    });
}

// ✅ دالة لجلب CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function clearCart() {
    localStorage.removeItem('cart');
    document.getElementById('cart').innerHTML = '';
    document.getElementById('total-price').textContent = 'الإجمالي: $0';
    alert('تم إفراغ السلّة بنجاح 🧹');
}

const express = require('express');
const mysql = require('mysql2');
const path = require('path');
const app = express();
const port = 3000;


// MySQL 연결
const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'As583346!@',
    database: 'pp'
});

db.connect((err) => {
    if (err) {
        console.error('MySQL 연결 실패:', err);
        return;
    }
    console.log('MySQL 연결 성공!');
});

// 정적 파일 제공 (index.html 등)
app.use(express.static(path.join(__dirname, 'public')));

// 상품 목록을 JSON 형식으로 제공
app.get('/products-data', (req, res) => {
    db.query('SELECT * FROM products', (err, results) => {
        if (err) {
            console.error('상품 불러오기 실패:', err);
            return res.status(500).json({ error: 'DB 오류' });
        }
        res.json(results);
    });
});

app.listen(port, () => {
    console.log(`서버 실행 중: http://localhost:${port}`);
});

app.get("/api/articles", async (req, res) => {
    const category = req.query.category;  // ex) "tech"
    let sql = "SELECT * FROM products";

    if (category && category !== "all") {
        sql += " WHERE category = ?";
        db.query(sql, [category], (err, results) => {
        if (err) return res.status(500).json({ error: err });
        res.json(results);
        });
    } else {
        db.query(sql, (err, results) => {
        if (err) return res.status(500).json({ error: err });
        res.json(results);
        });
    } 
});
db.movies.insertOne({
    "id": 6, 
    "title": "Avatar", 
    "genre": "Sci-Fi", 
    "year": 2009, 
    "rating": 7.9
});
db.movies.find({});
db.movies.find({ "genre": "Sci-Fi" });
db.movies.find({ "rating": { $gte: 8 } });
db.movies.updateOne(
    { "id": 3 },
    { $set: { "rating": 8.3 } }
);

db.movies.deleteOne({ "id": 4 });
db.movies.countDocuments({});
db.movies.find({}).sort({ "rating": -1 });
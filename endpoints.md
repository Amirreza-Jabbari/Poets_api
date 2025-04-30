
# Poets API Endpoints

---

## Hafez Endpoints

### Get Random Hafez Poem
```
GET /api/hafez/
```
Returns a random poem from Hafez's collection.

### Get Random Poem by Category
```
GET /api/hafez/{category}/
```
Returns a random poem from the specified category.

**Categories:**
- `ghazal` - Ghazals
- `ghete` - Ghete
- `robaee` - Robaee
- `ghaside` - Ghaside
- `montasab` - Montasab

### Get Specific Poem
```
GET /api/hafez/{category}/{number}/
```
Returns a specific poem by its category and number.

**Example:**
```
GET /api/hafez/ghazal/1/
```

---

## Khayyam Endpoints

### Get Random Khayyam Poem
```
GET /api/khayyam/
```
Returns a random poem from Khayyam's collection.

### Get Random Poem by Category
```
GET /api/khayyam/{category}/
```
Returns a random poem from the specified category.

**Categories:**
- `robaee` - Robaee
- `tarane` - Tarane

### Get Specific Poem
```
GET /api/khayyam/{category}/{number}/
```
Returns a specific poem by its category and number.

**Example:**
```
GET /api/khayyam/robaee/1/
```

---

## Moulavi (Rumi) Endpoints

### Get Random Moulavi Poem
```
GET /api/moulavi/
```
Returns a random poem from Moulavi's collection.

### Get Random Poem by Category
```
GET /api/moulavi/{category}/
```
Returns a random poem from the specified category.

**Categories:**
- `shams:ghazalsh` - Ghazals from Divan-e Shams
- `shams:mostadrakat` - Mostadrakat from Divan-e Shams
- `shams:tarjeeat` - Tarjeeat from Divan-e Shams
- `shams:robaeesh` - Robaee from Divan-e Shams
- `masnavi:daftar1` - Masnavi Book 1
- `masnavi:daftar2` - Masnavi Book 2
- `masnavi:daftar3` - Masnavi Book 3
- `masnavi:daftar4` - Masnavi Book 4
- `masnavi:daftar5` - Masnavi Book 5
- `masnavi:daftar6` - Masnavi Book 6

### Get Specific Poem
```
GET /api/moulavi/{category}/{number}/
```
Returns a specific poem by its category and number.

**Example:**
```
GET /api/moulavi/masnavi:daftar1/1/
```

---

## Golestan saadi Endpoints

### Get Random Hekayat
```
GET /api/golestan/
```
Returns a random hekayat from Golestan.

### Get Random Hekayat by Bab
```
GET /api/golestan/{bab}/
```
Returns a random hekayat from the specified bab (chapter).

**Bab Numbers:**
- `1` - Bab Aval (باب اول)
- `2` - Bab Dovom (باب دوم)
- `3` - Bab Sevom (باب سوم)
- `4` - Bab Chaharom (باب چهارم)
- `5` - Bab Panjom (باب پنجم)
- `6` - Bab Sheshom (باب ششم)
- `7` - Bab Haftom (باب هفتم)
- `8` - Bab Hashtom (باب هشتم)

### Get Specific hekayat
```
GET /api/golestan/{bab}/{hekayat}/
```
Returns a specific hekayat by its bab and hekayat number.

**Example:**
```
GET /api/golestan/1/1/
```

---

## Response Format

All API responses are in JSON format and typically include the following fields:

- For Hafez, Khayyam, and Moulavi:
  - `urn`: The unique identifier for the poem
  - `text`: The text content of the poem
  - Additional metadata specific to each poet

- For Golestan hekayat:
  - `bab`: The chapter number
  - `hekayat`: The hekayat number
  - `text`: The text content of the hekayat

---

## Error Responses

The API returns appropriate HTTP status codes:

- `400 Bad Request`: When an invalid category or parameter is provided
- `404 Not Found`: When the requested poem or hekayat doesn't exist

Error responses include a detail message explaining the error.

Example:
```json
{
  "detail": "Invalid category"
}
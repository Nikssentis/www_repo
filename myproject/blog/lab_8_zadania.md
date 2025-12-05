1. Pobranie posta po ID

{
postById(id: 5) {
id
title
text
slug
}
}

2. Wyszukiwanie postów po fragmencie tytułu

{
postsByTitle(substr: "1") {
id
title
text
}
}

3. Pobranie wszystkich kategorii

{
allCategories {
id
name
}
}

4. Pobranie wszystkich tematów (Topics)

{
allTopics {
id
name
category {
id
name
}
}
}

5. Zliczanie postów użytkownika

{
postCountByUser(userId: 1)
}

6. Zwracanie postów konkretnego użytkownika

{
postsByUser(userId: 1) {
id
title
text
}
}

7. Wyszukiwanie postów po fragmencie tekstu

{
postsByText(substr: "1") {
id
title
text
}
}

8. Pobieranie postów z danego topicu

{
postsByTopic(topicId: 4) {
id
title
text
}
}

9. Tworzenie posta

mutation {
createPost(
title: "Testowy post"
text: "Zawartość"
topicId: 5
slug: "testowy-post"
userId: 1
) {
post {
id
title
}
}
}

10. Edycja posta

mutation {
updatePost(
id: 5
title: "Nowy tytuł"
text: "Nowy tekst"
) {
post {
id
title
text
}
}
}

11. Usuwanie posta

mutation {
deletePost(id: 5) {
ok
}
}


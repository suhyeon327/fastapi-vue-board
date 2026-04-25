<!-- filename: frontend/src/App.vue -->
<script setup lang="ts">
</script>

<template>
  <header>
    <h1>FastAPI + Vue 게시판</h1>
    <nav>
      <RouterLink to="/">홈</RouterLink>
      <RouterLink to="/posts/new">새 글 작성</RouterLink>
    </nav>
  </header>
  <main>
    <RouterView />
  </main>
</template>
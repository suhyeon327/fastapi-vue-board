<!-- filename: frontend/src/views/PostDetailView.vue -->
<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '@/api'

interface Post {
  id: number
  title: string
  content: string
  created_at: string
}

const route = useRoute()
const router = useRouter()
const post = ref<Post | null>(null)

onMounted(async () => {
    try {
        const response = await api.get(`/posts/${route.params.id}`)
        post.value = response.data
    } catch (error) {
        console.error('게시글 로드 실패:', error)
        router.push('/')
    }
})

async function deletePost() {
    if (confirm('정말 삭제하시겠습니까?')) {
        await api.delete(`/posts/${route.params.id}`)
        router.push('/')
    }
}
</script>

<template>
    <div v-if="post">
        <h2>{{ post.title }}</h2>
        <p>{{ post.content }}</p>
        <p>작성일: {{ new Date(post.created_at).toLocaleDateString() }}</p>
        <RouterLink :to="`/posts/${post.id}/edit`">수정</RouterLink>
        <button @click="deletePost">삭제</button>
        <button @click="router.push('/')">목록으로</button>
    </div>
    <p v-else>로딩 중...</p>
</template>
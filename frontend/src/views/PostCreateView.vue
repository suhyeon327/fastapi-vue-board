<!-- filename: frontend/src/views/PostCreateView.vue -->
<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '@/api'

const router = useRouter()
const title = ref('')
const content = ref('')
const isSubmitting = ref(false)

async function handleSubmit() {
    isSubmitting.value = true
    try {
        await api.post('/posts', {
            title: title.value,
            content: content.value,
        })
        router.push('/')
    } catch (error) {
        console.error('작성 실패:', error)
        alert('게시글 작성에 실패했습니다.')
    } finally {
        isSubmitting.value = false
    }
}
</script>

<template>
    <h2>새 게시글</h2>
    <form @submit.prevent="handleSubmit">
        <div>
            <label>제목</label>
            <input v-model="title" required minlength="2" maxlength="100" />
        </div>
        <div>
            <label>내용</label>
            <textarea v-model="content" required></textarea>
        </div>
        <button type="submit" :disabled="isSubmitting">
            {{ isSubmitting ? '등록 중...' : '등록' }}</button>
    </form>
</template>
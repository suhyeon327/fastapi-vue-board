<!-- filename: frontend/src/views/PostEditView.vue -->
<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '@/api'

const route = useRoute()
const router = useRouter()
const title = ref('')
const content = ref('')
const isSubmitting = ref(false)

onMounted(async () => {
    const response = await api.get(`/posts/${route.params.id}`)
    title.value = response.data.title
    content.value = response.data.content
})

async function handleSubmit() {
    isSubmitting.value = true
    try {
        await api.put(`/posts/${route.params.id}`, {
            title: title.value,
            content: content.value,
        })
        router.push(`/posts/${route.params.id}`)
    } catch (error) {
        console.error('수정 실패:', error)
        alert('게시글 수정에 실패했습니다.')
    } finally {
        isSubmitting.value = false
    }
}
</script>

<template>
    <h2>게시글 수정</h2>
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
            {{ isSubmitting ? '수정 중...' : '수정' }}
        </button>
        <button type="button" @click="router.back()">취소</button>
    </form>
</template>
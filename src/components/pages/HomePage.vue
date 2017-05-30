<template>
  <div class="main-page">
    <h2 class="title">AppointmentGuru DocumentGuru</h2>
    <image-uploader ></image-uploader>
    <document-list></document-list>
  </div>
</template>

<script>
import ImageUploader from '@/components/ImageUploader'
import DocumentList from '@/components/DocumentList'

export default {
  name: 'homepage',
  props: ['documents'],
  components: {
    ImageUploader,
    DocumentList
  }
}
</script>
<style>
.title {
  text-align: center;
  font-style: italic;
  color: orangered;
}
</style>


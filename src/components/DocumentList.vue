<template>
<div>
  <strong>Todo</strong>
  <ul>
    <li>Ability to filter document list</li>
    <li>Ability to search document list</li>
  </ul>

  <strong>Listitem todo</strong>
  <ul>
    <li>Make it look nice</li>
  </ul>
  <document-list-item
    v-for='document in documents'
    :key='document.id'
    :document='document' >
  </document-list-item>
</div>
</template>
<script>
import DocumentListItem from './DocumentListItem'
export default {
  name: 'DocumentList',
  components: { DocumentListItem },
  props: {
    documents: { type: Array, required: true }
  }
}
</script>

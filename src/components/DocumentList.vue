<template>
<div>
  <div>
  <el-input
  placeholder="Search by id ex 1"
  icon="search"
  v-model="input2"
  :on-icon-click="handleIconClick">
</el-input>
  </div>
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
    :document='document' 
    :repeat='document' >
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
  },
  data () {
    return {
      input2: ''
    }
  },
  methods: {
    handleIconClick (ev) {
      console.log(ev)
    }
  }
}
</script>

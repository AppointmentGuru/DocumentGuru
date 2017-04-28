<template>
<div>
  {{document.name}}
</div>
</template>
<script>
export default {
  name: 'DocumentListItem',
  props: {
    document: { type: Object, required: true }
  }
}
</script>

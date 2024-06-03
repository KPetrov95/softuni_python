function editElement(ref, match, replace) {
    const refContentElement = ref.textContent;
    const matcher = new RegExp(match, 'g');
    const replacement = refContentElement.replace(matcher, replace)
    ref.textContent = replacement
}
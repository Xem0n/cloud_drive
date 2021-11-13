import './Submit.css';

type SubmitProps = {
    value: string;
};

const Submit = (props: SubmitProps) => (
    <input 
        className='input-submit'
        type='submit' 
        value={props.value} />
);

export default Submit;